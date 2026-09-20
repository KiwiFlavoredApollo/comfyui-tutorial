import random
from pathlib import Path

from comfy_sdk import Comfy

class CatVTONGenerator:
    def __init__(self):
        pass

    def run(self):
        client = Comfy()

        workflow = client.workflows.from_file(Path("input") / "catvton-tutorial.json")
        workflow.set_input("1", "seed", random.randint(1, 9223372036854775807))

        original = client.assets.from_file(Path("input") / "original.png")
        reference = client.assets.from_file(Path("input") / "reference.png")

        workflow.set_input("42", "image", original)
        workflow.set_input("52", "image", reference)

        job = client.run(workflow)

        for output in job.get_outputs("8"):
            output.to_file(Path("output") / output.name)