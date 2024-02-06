import cv2
import numpy
# 读取视频
cap = cv2.VideoCapture('input_video.mp4')

# 获取视频的帧率和尺寸
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置输出视频的格式
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (width, height))

# 设置裁剪的起始和结束帧
start_frame = 100
end_frame = 200

# 当前帧计数
current_frame = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 检查当前帧是否在裁剪区间内
    if start_frame <= current_frame <= end_frame:
        out.write(frame)

    current_frame += 1

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
