function goHome() {
    location.href = "/index.html";
}

function setFieldValue(id, value) {
    var element = document.getElementById(id);
    if (element) {
        element.innerHTML = value;
    }
}

function getFieldValue(id) {
    var element = document.getElementById(id);
    if (element) {
        return element.value;
    } else {
        return "";
    }
}

function showElement(id) {
    var element = document.getElementById(id);
    if (element) element.style.display = "block";
}
function hideElement(id) {
    var element = document.getElementById(id);
    if (element) element.style.display = "none";
}

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}