def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):   
    # ここから記述
    while True:
        #配列の真ん中を変数centerに格納
        center = int(len(sorted_array)/2)
        #真ん中の値とtarget_numberの値を比べる
        #真ん中の値よりtargetが小さかったとき
        if sorted_array[center] > target_number:
            #配列の真ん中まででtargetを探索
            for num in range(center):
                #targetを見つけたとき
                if sorted_array[num] == target_number:
                    return num
                else:
                    continue
        #真ん中よりtargetが大きかったとき
        elif sorted_array[center] <= target_number:
            #真ん中の値とtarget_numberの値を比べる
            #真ん中の値よりtargetが小さかったとき
            for num in range(center,len(sorted_array)-1):
                #targetを見つけたとき
                if sorted_array[num] == target_number:
                    return num
                else:
                    continue

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
