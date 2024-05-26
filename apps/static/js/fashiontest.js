//ボタンを押すごとに画面が切り替わる関数
  $(function () {

    $(".btn").on("click", function () {
      $(this).closest("div").css("display", "none");
      id = $(this).attr("href");
      $(id).addClass("fit").fadeIn("slow").show();
    });



//選択ボタンデータを配列に入れてカウントする関数
      var countA;
      var countB;
      var countC;
      var countD;
      var box =[];
    $(".btn").each(function(){
      $(this).on('click',function(){
        var value = $(this).data("value");
         box.push(value);

        countA = box.filter(function(x){
                      return x === "a"
                    }).length;
        countB = box.filter(function(y){
                        return y === "b"
                    }).length;
        countC = box.filter(function(t){
                      return t === "c"
                    }).length;
        countD = box.filter(function(h){
                        return h === "d"
                    }).length;
      });
    });


//結果を出力する関数
    $('.end').on('click',function(){
      if(( countA > countB )&&( countC == countD )) {
        $('#answer_01').css("display",""); //回答1
      } else if(( countB > countA )&&( countC == countD )) {
        $('#answer_02').css("display","");//回答2
      } else if(( countC > countD )&&( countA == countB )) {
        $('#answer_03').css("display",""); //回答1
      } else {
        $('#answer_04').css("display","");//回答2
    }
  });
  });