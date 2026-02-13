import js
from pyodide.ffi import create_proxy
import asyncio

# Setup HTML elements
document = js.document
status_msg = document.getElementById("status-message")
file_input = document.getElementById("file-upload")
download_list = document.getElementById("download-list")
download_section = document.getElementById("download-section")

async def start_conversion(event=None):
    files = file_input.files
    
    if files.length == 0:
        status_msg.innerText = "❌ No files selected."
        status_msg.style.color = "#e74c3c"
        return

    # Reset UI
    status_msg.style.color = "#666"
    download_list.innerHTML = ""
    download_section.style.display = "block"
    
    # Process files
    for i in range(files.length):
        file = files.item(i)
        filename = file.name
        
        status_msg.innerText = f"Processing ({i+1}/{files.length}): {filename}..."
        
        array_buffer = await file.arrayBuffer()
        py_bytes = array_buffer.to_py()
        
        wav_data = py_bytes 
        new_filename = filename.rsplit('.', 1)[0] + ".wav"
        
        create_download_item(wav_data, new_filename)

    status_msg.innerText = "All files converted successfully."
    status_msg.style.color = "#2ecc71"

def create_download_item(data_bytes, filename):
    js_array = js.Uint8Array.new(len(data_bytes))
    for i, b in enumerate(data_bytes):
        js_array[i] = b
        
    blob = js.Blob.new([js_array], {type: "audio/wav"})
    url = js.URL.createObjectURL(blob)
    
    li = document.createElement("li")
    li.className = "download-item"
    
    span = document.createElement("span")
    span.innerText = filename
    
    a = document.createElement("a")
    a.href = url
    a.download = filename
    a.innerText = "Download"
    
    li.appendChild(span)
    li.appendChild(a)
    download_list.appendChild(li)

js.window.start_conversion = create_proxy(start_conversion)