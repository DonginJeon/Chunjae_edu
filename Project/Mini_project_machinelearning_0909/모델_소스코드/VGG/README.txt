VGG16을 이용한 모델

1. 제출파일 > 모델_소스코드 > VGG 
    
    model_factory1.ipynb(처음 모델 학습), 
    
    model_factory2.ipynb(가중치 수정한 모델 학습),
    
    load_model.ipynb (학습된 모델 임포트, 테스트 샘플 테스트, 혼동 행렬 시각화),
    
    best_model.keras(처음 모델)
    
    best_model2.keras(수정 모델)
    
    VGG 폴더 아래에 data 폴더를 만들고 그 안에 학습용(폴더명 : train_added), 검증용(폴더명 : validation), 테스트용(폴더명 : test) 샘플이 들어 있는 폴더를 넣고 소스 코드 파일을 실행시키면 됩니다.
    
    load_model 파일을 실행할 땐 두 번째 셀의 load_model() 안에 로드할 모델 이름을 수정하고 실행하면 됩니다.