from fastapi import FastAPI
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from fastapi.responses import FileResponse

app = FastAPI()

model_id = "stabilityai/stable-diffusion-2-1"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe = pipe.to("cuda")

@app.get("/vector_image")
def image_endpoint(prompt):

    image = pipe(prompt, num_inference_steps=10).images[0]
    image.save("image.png")
    return FileResponse("image.png")