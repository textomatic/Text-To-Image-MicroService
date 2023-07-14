from diffusers import StableDiffusionPipeline
import torch

model_id = "prompthero/openjourney-v4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
prompt = "retro serie of different cars with different colors and shapes, mdjrny-v4 style"
image = pipe(prompt, num_inference_steps=1).images[0]
#image.save("retro_cars.png")