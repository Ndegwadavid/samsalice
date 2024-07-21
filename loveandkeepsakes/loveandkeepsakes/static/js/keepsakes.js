document.addEventListener('DOMContentLoaded', function() {
    const textInput = document.getElementById('text-input');
    const fontSelect = document.getElementById('font-select');
    const fontSize = document.getElementById('font-size');
    const colorPicker = document.getElementById('color-picker');
    const imageColor = document.getElementById('image-color');
    const previewBtn = document.getElementById('preview-btn');
    const buyBtn = document.getElementById('buy-btn');
    const textOverlay = document.getElementById('text-overlay');
    const engravableImage = document.getElementById('engravable-image');
    const imageOptions = document.querySelectorAll('.image-option');
    const emojiOptions = document.querySelectorAll('.emoji-option');
    const borderRadius = document.getElementById('border-radius');
    const imageContainer = document.getElementById('image-container');

    function updateTextOverlay() {
        textOverlay.style.fontFamily = fontSelect.value;
        textOverlay.style.fontSize = `${fontSize.value}px`;
        textOverlay.style.color = colorPicker.value;
        textOverlay.textContent = textInput.value;
    }

    function changeImage(imageSrc) {
        engravableImage.src = imageSrc;
        imageOptions.forEach(img => img.classList.remove('selected'));
        event.target.classList.add('selected');
    }

    function addEmoji(emoji) {
        textInput.value += emoji;
        updateTextOverlay();
    }

    function applyColorFilter() {
        const color = imageColor.value;
        engravableImage.style.filter = `opacity(0.8) drop-shadow(0 0 0 ${color})`;
    }

    function updateBorderRadius() {
        imageContainer.style.borderRadius = `${borderRadius.value}px`;
    }

    textInput.addEventListener('input', updateTextOverlay);
    fontSelect.addEventListener('change', updateTextOverlay);
    fontSize.addEventListener('input', updateTextOverlay);
    colorPicker.addEventListener('input', updateTextOverlay);
    imageColor.addEventListener('input', applyColorFilter);
    borderRadius.addEventListener('input', updateBorderRadius);

    imageOptions.forEach(img => {
        img.addEventListener('click', function() {
            changeImage(this.src);
        });
    });

    emojiOptions.forEach(emoji => {
        emoji.addEventListener('click', function() {
            addEmoji(this.textContent);
        });
    });

    previewBtn.addEventListener('click', function() {
        updateTextOverlay();
        applyColorFilter();
        updateBorderRadius();
        alert('This is your current preview. In a real implementation, we would generate a high-quality preview image.');
    });

    buyBtn.addEventListener('click', function() {
        alert('Thank you for your purchase! In a real implementation, this would process the order.');
    });

    // Initialize the text overlay
    updateTextOverlay();
    updateBorderRadius();
});
