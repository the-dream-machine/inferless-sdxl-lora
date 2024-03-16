import json
import numpy as np
import torch
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
import base64
from io import BytesIO


class InferlessPythonModel:
    """
    Class for text-to-image generation using Stable Diffusion with LORA guidance, optimized for inference speed.
    """

    def initialize(self):
        """
        Initializes the model, scheduler, and loads model weights.
        """
        model_id = "stabilityai/stable-diffusion-xl-base-1.0"
        lora_id = "artificialguybr/LogoRedmond-LogoLoraForSDXL-V2"

        # Load the diffusion model with FP16 precision for efficiency
        self.pipe = DiffusionPipeline.from_pretrained(model_id, variant="fp16")

        # Use the high-performance DPMSolver++ scheduler for faster inference
        scheduler = DPMSolverMultistepScheduler(use_karras_sigmas=True, algorithm_type="sde-dpmsolver++")
        self.pipe.scheduler = scheduler.from_config(self.pipe.scheduler.config)

        # Load LORA weights for text-based guidance
        self.pipe.load_lora_weights(lora_id)

        # Move model to GPU for faster processing
        if torch.cuda.is_available():
            self.pipe.to(device="cuda", dtype=torch.float16)

    def infer(self, inputs):
        """
        Generates an image based on the provided prompt.
        """
        prompt = inputs["prompt"]

        # Generate the image using the model with 30 inference steps and full guidance scale
        pipeline_output_image = self.pipe(
            prompt=prompt,
            num_inference_steps=30,
            guidance_scale=1,
        ).images[0]

        # Encode the generated image as a base64 string for convenient transfer
        buff = BytesIO()
        pipeline_output_image.save(buff, format="PNG")
        img_str = base64.b64encode(buff.getvalue())
        return {"generated_image_base64": img_str.decode("utf-8")}

    def finalize(self, args):
        """
        Cleans up model resources to prevent memory leaks.
        """
        self.pipe = None
