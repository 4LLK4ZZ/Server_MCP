from fastmcp import FastMCP, Image
from PIL import Image as PILImage
import io

mcp = FastMCP("Image Demo")

@mcp.tool()
def create_thumbnail(image_data: Image) -> Image:
    """Creates a 100x100 thumbnail from the provided image."""
    img = PILImage.open(io.BytesIO(image_data.data)) # Assumes image_data received as Image with bytes
    img.thumbnail((100, 100))
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    # Return a new Image object with the thumbnail data
    return Image(data=buffer.getvalue(), format="png")

@mcp.tool()
def load_image_from_disk(path: str) -> Image:
    """Loads an image from the specified path."""
    # Handles reading file and detecting format based on extension
    return Image(path=path)