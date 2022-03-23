import tkinter
import tkinter.ttk

def headtable():
# ﻿GUI창을 생성라벨 설정
    root=tkinter.Tk()
    root.title("머리 아플때 추천 약")
    root.geometry("1100x400+100+100")
    root.resizable(False, False)

    lbl = tkinter.Label(root, text="추천약물")
    lbl.pack()

# ﻿표 생성하기.
    treeview=tkinter.ttk.Treeview(root, columns=["one", "two","three","four"],
                                  displaycolumns=["one","two","three","four"])
    treeview.pack()

# 각 컬럼 설정.  이름,  넓이, 정렬
    treeview.column("#0", width=70,)
    treeview.heading("#0", text="추천순위")
    
    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="약물이름", anchor="center")
    
    treeview.column("#2", width=300, anchor="center")
    treeview.heading("two", text="기능", anchor="center")

    treeview.column("#3", width=200, anchor="center")
    treeview.heading("three", text="성분", anchor="center")

    treeview.column("#4", width=400, anchor="center")
    treeview.heading("four", text="부작용", anchor="center")
    # 표에 삽입될 데이터
    treelist=[("타이레놀", '해열진통', '아세트아미노펜,파라세타몰',"없음"
), ("아스피린", '진통효과 및 소염효과', '아세틸살리실산',"위염이나 위궤양처럼 위가 안좋은 사람은 과다출혈의 부작용"
), ("게보린", '해열진통', '이소프로필안티피린',"과림구감소증"
), ("나프록센", '염증부위 삼출물억제,진통,소염작용', '나프록센',"위장에 무리를 줄수있어 속쓰림유발"
), ("덱시부프로펜", '소염', '덱시부프로펜',"없음"
)]
    
    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i+1, values=treelist[i], iid=str(i)+"번")
   # GUI 실행
    root.mainloop()
    
######################################################################################보기좋게 나누기


def mutable():
# ﻿GUI창을 생성라벨 설정
    root=tkinter.Tk()
    root.title("근육통 추천 약")
    root.geometry("1100x400+100+100")
    root.resizable(False, False)

    lbl = tkinter.Label(root, text="추천약물")
    lbl.pack()

# ﻿표 생성하기.
    treeview=tkinter.ttk.Treeview(root, columns=["one", "two","three","four"],
                                  displaycolumns=["one","two","three","four"])
    treeview.pack()

# 각 컬럼 설정.  이름,  넓이, 정렬
    treeview.column("#0", width=70,)
    treeview.heading("#0", text="추천순위")
    
    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="약물이름", anchor="center")
    
    treeview.column("#2", width=300, anchor="center")
    treeview.heading("two", text="기능", anchor="center")

    treeview.column("#3", width=200, anchor="center")
    treeview.heading("three", text="성분", anchor="center")

    treeview.column("#4", width=400, anchor="center")
    treeview.heading("four", text="부작용", anchor="center")
    
    # 표에 삽입될 데이터
    treelist=[("타마돌", '중증도 동통,수술후 동통감소', '트마라돌염산염',"없음"
), ("아섹정", '관절염,척추염,외상후 염증으로인한 통증감소', '아세클로페낙',"과민증,소화기계 이상"
), ("게보린", '해열진통', '이소프로필안티피린',"위장이상반응, 어지러움,간효소수치이상"
), ("록소프로", '요통, 류마티스관절염,퇴행성관절염 통증감소', '록소프로펜',"쇼크, 소화기계이상"
)]
    
    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i+1, values=treelist[i], iid=str(i)+"번")
   # GUI 실행
    root.mainloop()

######################################################################################보기좋게 나누기


def smatable():
# ﻿GUI창을 생성라벨 설정
    root=tkinter.Tk()
    root.title("소화불량 추천 약")
    root.geometry("1100x400+100+100")
    root.resizable(False, False)

    lbl = tkinter.Label(root, text="추천약물")
    lbl.pack()

# ﻿표 생성하기.
    treeview=tkinter.ttk.Treeview(root, columns=["one", "two","three","four"],
                                  displaycolumns=["one","two","three","four"])
    treeview.pack()

# 각 컬럼 설정.  이름,  넓이, 정렬
    treeview.column("#0", width=70,)
    treeview.heading("#0", text="추천순위")
    
    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="약물이름", anchor="center")
    
    treeview.column("#2", width=300, anchor="center")
    treeview.heading("two", text="기능", anchor="center")

    treeview.column("#3", width=200, anchor="center")
    treeview.heading("three", text="성분", anchor="center")

    treeview.column("#4", width=400, anchor="center")
    treeview.heading("four", text="부작용", anchor="center") 
    # 표에 삽입될 데이터
    treelist=[("베스타제", '소화불량,식욕감퇴,과식,식체 완화', '비오디아스타제,셀룰라제',"없음"
), ("훼스탈", '소화불량,위부팽만감 완화', '셀룰라제,판크레아틴',"알레르기,입이마름"
), ("까스활명수", '소화불량,식체,구토 등 완화', '육계,진피',"없음"
), ("큐자임", '식욕감퇴 소화불량 고토 완화', 'DL-카르니틴염산염',"위장실환환자 주의, 다량복용시 구토,피로감"
)]
    
    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i+1, values=treelist[i], iid=str(i)+"번")
   # GUI 실행
    root.mainloop()

######################################################################################보기좋게 나누기


def colictable():
# ﻿GUI창을 생성라벨 설정
    root=tkinter.Tk()
    root.title("배가 아플때 추천 약")
    root.geometry("1100x400+100+100")
    root.resizable(False, False)

    lbl = tkinter.Label(root, text="추천약물")
    lbl.pack()

# ﻿표 생성하기.
    treeview=tkinter.ttk.Treeview(root, columns=["one", "two","three","four"],
                                  displaycolumns=["one","two","three","four"])
    treeview.pack()

# 각 컬럼 설정.  이름,  넓이, 정렬
    treeview.column("#0", width=70,)
    treeview.heading("#0", text="추천순위")
    
    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="약물이름", anchor="center")
    
    treeview.column("#2", width=300, anchor="center")
    treeview.heading("two", text="기능", anchor="center")

    treeview.column("#3", width=200, anchor="center")
    treeview.heading("three", text="성분", anchor="center")

    treeview.column("#4", width=400, anchor="center")
    treeview.heading("four", text="부작용", anchor="center")

    
    # 표에 삽입될 데이터
    treelist=[("부스코판", '위경련,위염,장염 감소', '부틸스코폴라민브롬화물',"없음"
), ("알피움", '위장관계의 경련 및 기능적운동장애 완화', 'tla시메트로퓸브롬화물',"노인주의:항콜린부작용(변비,배뇨골곤란)"
), ("스파토민", '위염,대장염,경련성변비에 효과', '디시클로민산염',"없음"
), ("후로스판", '비뇨기계의 경련 및 통증완화', '플로로글루시놀수화물',"급성전신성발진성농포증"
)]
    
    # 표에 데이터 삽입
    for i in range(len(treelist)):
        treeview.insert('', 'end', text=i+1, values=treelist[i], iid=str(i)+"번")
   # GUI 실행
    root.mainloop()

