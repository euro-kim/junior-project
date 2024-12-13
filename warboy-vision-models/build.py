import cv2
import os
import argparse

def create_video(input_folder, output_video, frame_rate):
    # BMP 파일을 정렬하여 읽어들임
    bmp_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.bmp')])

    if not bmp_files:
        print("Error: No BMP files found in the specified directory.")
        return

    # 첫 번째 BMP 파일로부터 이미지 크기 설정
    frame = cv2.imread(os.path.join(input_folder, bmp_files[0]))
    height, width, _ = frame.shape

    # 비디오 writer 객체 생성
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

    # BMP 파일을 순차적으로 읽어 비디오로 합침
    for bmp in bmp_files:
        img = cv2.imread(os.path.join(input_folder, bmp))
        out.write(img)

    # 비디오 파일 저장
    out.release()
    cv2.destroyAllWindows()

    print(f"동영상 생성 완료: {output_video}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a video from BMP images in a directory.")
    parser.add_argument("input_folder", type=str, help="Path to the folder containing BMP files.")
    parser.add_argument("output_video", type=str, nargs='?', default="output_video.avi", help="Name of the output video file.")
    parser.add_argument("--frame_rate", type=int, default=30, help="Frame rate of the output video (default: 30).")

    args = parser.parse_args()

    create_video(args.input_folder, args.output_video, args.frame_rate)
