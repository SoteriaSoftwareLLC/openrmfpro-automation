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

function getStatusBadge(status) {
    if (status.toLowerCase() == "open")
      return '<span class="badge rounded-capsule badge-soft-danger fs--2">Open</span>';
    else if (status.toLowerCase() == "not_applicable" || status.toLowerCase() == "not applicable" )
      return '<span class="badge rounded-capsule badge-soft-secondary fs--2">N/A</span>';
    else if (status.toLowerCase() == "not_reviewed" || status.toLowerCase() == "not reviewed")
      return '<span class="badge rounded-capsule badge-soft-dark fs--2">Not Reviewed</span>';
    else if (status.toLowerCase() == "notafinding" || status.toLowerCase() == "not a finding") // Not a Finding
      return '<span class="badge rounded-capsule badge-soft-success fs--2">Not a Finding</span>';
      else
        return '<span class="badge rounded-capsule fs--2">' + status + '</span>'; // generic catch all
  }
  
  function getSeverityBadge(severity) {
      if (severity.toLowerCase() == "high" || severity.toLowerCase() == "critical")
          return '<span class="badge rounded-capsule badge-soft-danger fs--2">CAT I</span>';
      else if (severity.toLowerCase() == "medium")
          return '<span class="badge rounded-capsule badge-soft-warning fs--2">CAT II</span>';
      else // this is low
          return '<span class="badge rounded-capsule badge-soft-cat3 fs--2">CAT III</span>';
  }