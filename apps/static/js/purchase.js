// // ボタン要素を取得
// var playButton = document.getElementById('playButton');

// // オーディオ要素を取得
// var audioElement = document.getElementById('audioElement');

// // ボタンがクリックされたときの処理
// playButton.addEventListener('click', function() {
//     // 音声を再生

//     audioElement.play();

//     setTimeout(function() {
//         // 遷移先のURLを設定
//         window.location.href = 'purchase.html'; // 遷移先のURLを指定
//     }, 4000);

// });

function redirectToSelected() {
  // ラジオボタンの要素を取得
  var radioButtons = document.getElementsByName("payment");
  // var radioButtons = document.getElementsByID('audioOption');
  var selectedOption = null;

  // 選択されたラジオボタンを確認
  for (var i = 0; i < radioButtons.length; i++) {
    if (radioButtons[i].checked) {
      selectedOption = radioButtons[i].value;
      break;
    }
  }

  // ラジオボタンが選択されているか確認
  if (selectedOption !== null) {
    // 対応する音声を再生
    document
      .getElementById(
        "audio" + selectedOption.charAt(selectedOption.length - 1)
      )
      .play();

    // 3秒後に画面遷移
    setTimeout(function () {
      // 遷移先のURLを設定
      // window.location.href = 'purchase.html'; // 遷移先のURLを指定
    }, 3000);
  }
}

// キャンセルボタン追加
function redirectToPage() {
  // window.location.href = "purchase.html";
  history.back();
}

// function redirectToSelected() {
//     var radios = document.getElementsByName('payment');

//     for (var i = 0; i < radios.length; i++) {
//         if (radios[i].checked) {
//             location.href = radios[i].value;
//             break;
//         }
//     }
// }

// function playSound(soundFile) {
//     var audio = document.getElementById('audio');
//     audio.src = soundFile;
//     audio.play();
// }

// card_form.html
// function redirectToPage() {

//     window.location.href = "purchase.html";
//   }
