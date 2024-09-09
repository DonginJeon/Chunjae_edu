### 말과 사람 이미지 분류 모델
- TensorFlow와 Keras를 사용하여 말과 사람 이미지를 분류하는 딥러닝 모델을 구현합니다. 
- 말과 사람 이미지 데이터셋을 사용하여 모델을 학습시키고, loss 및 accuracy와 혼동 행렬을 통해 성능을 평가합니다.
---
#### 필요한 패키지 list
- Python 3.xx
- TensorFlow
- Keras
- OpenCV
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pandas
- => 다음 명령어로 패키지를 설치할 수 있습니다: pip install tensorflow opencv-python numpy matplotlib seaborn scikit-learn pandas
---
#### 데이터셋 구조
- train_added/horses: 말 이미지가 저장된 학습 데이터 디렉토리.
- train_added/humans: 사람 이미지가 저장된 학습 데이터 디렉토리.
- valid: 모델 평가를 위한 검증 데이터 디렉토리.
- test12: 예측을 위한 테스트 이미지 디렉토리.

#### 코드 개요
1. 데이터 준비:
- 학습 디렉토리의 이미지 수를 세고 목록화함.
- 샘플 이미지 미리보기로 표시.
2. 모델 설계:
- 여러 컨볼루션 및 풀링 레이어를 포함한 Sequential CNN 모델을 설계.
- 이진 교차 엔트로피 손실 함수와 Adam 옵티마이저로 컴파일.
3. 데이터 증강: ImageDataGenerator를 사용하여 이미지를 스케일링.
4. 모델 학습: early stopping과 모델 checkpoint callback을 사용하여 모델 학습시키기.
5. 평가:
- 모델의 정확도와 손실 시각화.
- 검증 세트를 사용하여 모델을 평.
6. 예측:
- 테스트 디렉토리의 이미지를 처리하고, 클래스를 예측.
- 혼동 행렬을 통해 예측 결과를 시각화.
