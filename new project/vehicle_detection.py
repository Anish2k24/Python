import cv2
import pandas as pd

def load_vehicle_data(csv_path):
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"error loading csv: {e}")
        return None

def dummy_vehicle_detector(image):
    height, width, _ = image.shape
    detections = [
        {"id": 0, "box": (int(0.1 * width), int(0.2 * height), int(0.3 * width), int(0.3 * height))},
        {"id": 1, "box": (int(0.5 * width), int(0.4 * height), int(0.4 * width), int(0.4 * height))}
    ]
    return detections

def match_vehicle_details(detections, vehicle_data):
    matched_details = []
    for det in detections:
        vehicle_id = det["id"]
        if vehicle_id < len(vehicle_data):
            details = vehicle_data.iloc[vehicle_id].to_dict()
            matched_details.append((det, details))
        else:
            matched_details.append((det, None))
    return matched_details

def main():
    csv_path = "Vehicle Detection.csv"
    image_path = "trafic2.jpg"
    
    vehicle_data = load_vehicle_data(csv_path)
    if vehicle_data is None:
        return
    
    image = cv2.imread(image_path)
    if image is None:
        print(f"error: could not load image from {image_path}")
        return
    
    detections = dummy_vehicle_detector(image)
    
    for det in detections:
        x, y, w_box, h_box = det["box"]
        cv2.rectangle(image, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
        cv2.putText(image, f"vehicle {det['id']}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    cv2.imshow("detected vehicles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    matched = match_vehicle_details(detections, vehicle_data)
    for det, details in matched:
        print("=" * 40)
        print(f"detected vehicle id: {det['id']}")
        if details:
            print(f"name: {details.get('name', 'n/a')}")
            print(f"model: {details.get('model', 'n/a')}")
            print(f"manufacturing date: {details.get('manufacturing_date', 'n/a')}")
        else:
            print("no details available for this vehicle.")
        print("=" * 40)

if __name__ == "__main__":
    main()
