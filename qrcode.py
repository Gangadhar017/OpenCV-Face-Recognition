import cv2
from pyzbar.pyzbar import decode

def scan_qr_code():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        decoded_objects = decode(frame)
        for obj in decoded_objects:
        
            qr_data = obj.data.decode('utf-8')
            print(f'Scanned QR Code Data: {qr_data}')
            break  
        cv2.imshow('QR Code Scanner', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '_main_':
    scan_qr_code()