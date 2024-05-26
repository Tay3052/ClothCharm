// スライドショーのための画像インデックス
let currentImageIndex = 0;

// 画像選択時に画像をプレビューする処理
document.getElementById("imageUpload").addEventListener("change", function(event) {
    const imagePreview = document.querySelector(".image-preview");
    const uploadedImages = document.querySelectorAll(".uploaded-image");

    // 既存のプレビューに新しい画像を追加
    for (let i = 0; i < event.target.files.length; i++) {
        const image = document.createElement("img");
        image.src = URL.createObjectURL(event.target.files[i]);
        image.classList.add("uploaded-image");
        imagePreview.appendChild(image);
    }

    // すべてのプレビューを非表示にし、最初の画像を表示
    uploadedImages.forEach((image, index) => {
        if (index === 0) {
            image.style.display = "block";
        } else {
            image.style.display = "none";
        }
    });

    // 画像が選択されたら前へと次へのボタンを有効化
    currentImageIndex = 0;
    showCurrentImage();
});

// 画像が選択された場合に前へと次へのボタンを表示
function showCurrentImage() {
    const images = document.querySelectorAll(".uploaded-image");
    const prevButton = document.getElementById("prevImage");
    const nextButton = document.getElementById("nextImage");

    if (images.length > 0) {
        images.forEach((image, index) => {
            if (index === currentImageIndex) {
                image.style.display = "block";
            } else {
                image.style.display = "none";
            }
        });

        prevButton.disabled = currentImageIndex === 0;
        nextButton.disabled = currentImageIndex === images.length - 1;
    } else {
        prevButton.disabled = true;
        nextButton.disabled = true;
    }
}

// 前へボタンのクリックイベント
document.getElementById("prevImage").addEventListener("click", function() {
    const images = document.querySelectorAll(".uploaded-image");
    if (currentImageIndex > 0) {
        currentImageIndex--;
        showCurrentImage();
    }
});

// 次へボタンのクリックイベント
document.getElementById("nextImage").addEventListener("click", function() {
    const images = document.querySelectorAll(".uploaded-image");
    if (currentImageIndex < images.length - 1) {
        currentImageIndex++;
        showCurrentImage();
    }
});
document.getElementById("imageUpload").addEventListener("change", function(event) {
    const imagePreview = document.querySelector(".image-preview");
    imagePreview.innerHTML = ""; // 既存のプレビューをクリア

    // 画像を選択し、それぞれの画像をプレビューに追加
    for (let i = 0; i < event.target.files.length; i++) {
        const image = document.createElement("img");
        image.src = URL.createObjectURL(event.target.files[i]);
        image.classList.add("uploaded-image");
        imagePreview.appendChild(image);
    }

    // 画像が選択されたら前へと次へのボタンを有効化
    currentImageIndex = 0;
    showCurrentImage();
});