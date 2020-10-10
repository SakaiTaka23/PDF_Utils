# PDF_Utils



 ## Apps

1. jpeg,pngから文字を読み取り変換する(img2txt)



2. 連番ファイルを受け取りそれらを任意の名前に変換する(name2anyname)
3. pdfのページを分割、連番として出力(spli2pdf)
4. 与えられたpdfを連番の画像として出力(pdf2img)
5. pdfから直接文字を読み取り出力(pdf2txt)



## img2txt

* ユーザーからは画像を入力として受け取る

* 原則として出力は連番とする

  

### 仕組み

1. ユーザーからファイルを受け取り、それが画像ファイルかどうか確認

そうでない場合はエラー、リダイレクト

2. そうである場合はランダムキーをつけてdbに保存 (パス：media/img2txt/task_id_*.img)

3. ランダムキーに基づき画像一枚一枚に対してid順にtxtファイルを連番で生成、再度メディアフォルダに保存(パス：media/img2txt/task_id_*.txt)

4. ダウンロード画面へ移動する

   与えられたidに対してそのidがつくtxtファイルをmediaから検索

   ファイルの番号からユーザーがどのファイルをダウンロードしたがっているか判断

   それらをmediaファイルから取得してzip化した上でユーザーにダウンロードさせる

5. ダウンロード→画像データ、テキストデータ、dbデータは削除



## name2anyname

* ユーザーからはファイルを受け取る

* 受け取ったファイルを任意の名前に変換する

  

### 仕組み

1. ユーザーからファイルを受け取り、拡張子は気にしない
2. 自然ソート し、ファイル名を取得
3. ユーザーから与えられたルールからファイル名を順番に作成
4. 名前変更

