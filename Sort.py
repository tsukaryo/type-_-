
def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)

    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]
    
    # ここから記述
    #入れかれる要素の値、インデックス、入れ替え要素を見つけたフラグを定義
    below_frag = 0
    above_frag = 0
    above_index = 0
    above_value = 0
    below_index = 0
    below_value = 0
    #最後にできた配列の確認をするフラグを定義
    frag=0

    j=0
    #ソートが終わるまで無限ループ
    while True:
        
        #一つずつ要素を確認
        for i in range(len(array)):
            #配列をはじめから見ていってpivot(基準)以上の要素を見つけたときにその値を記録
            if pivot <= array[i] and above_frag == 0:
                above_value = array[i]
                above_index = i
                above_frag = 1

            #配列を後ろから見ていってpivot(基準)未満の要素を見つけたときにその値を記録
            if pivot > array[-1-i] and below_frag == 0:
                below_value = array[-1-i]
                below_index = len(array) - i -1
                below_frag = 1

            #配列のソートが完了したときに再帰処理を行う
            if ((above_index - below_index > 0) and (above_frag == 1 and below_frag == 1)) or (i == len(array)-1 and (above_index == 0 and below_index == 0)):
                #基準値未満のみの配列で再帰処理して、結果をarrayに入れる
                array[0:below_index+1] = sort(array[0:below_index+1])
                #基準値以上のみの配列で再帰処理して、結果をarrayに入れる
                array[below_index+1:] = sort(array[below_index+1:])

                return array

            #fragが二つとも1となったときの入れ替え処理
            if above_frag == 1 and below_frag == 1:
                array[below_index] = above_value
                array[above_index] = below_value
                above_index,below_index = 0,0
                below_frag = 0
                above_frag = 0
                break
            
        #配列の確認作業　ソートが完了していたら抜ける
        for i in range(len(array)-1):
            if array[i+1]-array[i] <= 0:
                frag = 1
        if frag == 0:
            break
        frag = 0
        
  
    return array

    # ここまで記述

if __name__ == '__main__':
    main()