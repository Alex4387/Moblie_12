# …
from changedetection import ChangeDetection #added

# …
@torch.no_grad()
def run(
    weights=ROOT / 'yolov5s.pt', # model.pt path(s)
    
    # …
    cd = ChangeDetection(names) #added by kiokahn, 20220608
    
    # Run inference
    model.warmup(imgsz=(1 if pt else bs, 3, *imgsz)) # warmup
        detected = [0 for i in range(len(names))] #added by kiokahn, 20220608
    
        if len(det):
        # …
            # Write results
            for *xyxy, conf, cls in reversed(det):
                detected[int(cls)] = 1 #added by kiokahn, 20220608
        # …
        cd.add(names,detected,save_dir,im0) #added by kiokahn, 20220608
    
    if view_img:
    cv2.imshow(str(p), im0)