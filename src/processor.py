import os
import cv2
import pandas as pd
import numpy as np
from PIL import Image
from utils import get_project_root, ensure_dir

def run_processor():
    BASE_DIR = get_project_root()
    metadata_path = os.path.join(BASE_DIR, "data", "metadata.csv")
    processed_path = os.path.join(BASE_DIR, "data", "processed")
    
    if not os.path.exists(metadata_path):
        print("Error: metadata.csv not found. Run scraper.py first!")
        return

    # Ensure output folder exists
    ensure_dir(processed_path)
    
    df = pd.read_csv(metadata_path)
    stats = []
    print(f"Processing {len(df)} images...")

    for i, row in df.iterrows():
        try:
            # 1. Load & Resize (PIL Logic)
            img = Image.open(row['local_path'])
            resized = img.resize((200, 300))
            
            # 2. Grayscale & Edges (OpenCV Logic)
            # Convert PIL image to Grayscale Numpy array for OpenCV
            gray_array = np.array(resized.convert('L'))
            edges = cv2.Canny(gray_array, 100, 200)
            
            # 3. Save Processed Image
            proc_filename = f"edge_{i}.jpg"
            proc_file_path = os.path.join(processed_path, proc_filename)
            cv2.imwrite(proc_file_path, edges)
            
            # 4. Intelligence Gathering
            stats.append({
                "brightness": gray_array.mean(),
                "file_size_kb": os.path.getsize(row['local_path']) / 1024,
                "processed_path": proc_file_path
            })
            print(f"Processed: {proc_filename}")
            
        except Exception as e:
            print(f"Error at {row['title']}: {e}")

    # Merge results and update CSV
    stats_df = pd.DataFrame(stats)
    final_df = pd.concat([df, stats_df], axis=1)
    final_df.to_csv(metadata_path, index=False)
    print("\nProcessing complete! 'data/processed' is full and CSV is updated.")

if __name__ == "__main__":
    run_processor()