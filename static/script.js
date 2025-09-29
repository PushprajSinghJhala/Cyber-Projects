async function processText(action) {
  const text = document.getElementById("text").value;
  const method = document.getElementById("method").value;

  const response = await fetch(`/${action}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: text, method: method })
  });

  const data = await response.json();
  document.getElementById("result").value = data.result;
}

function copyResult() {
  const result = document.getElementById("result");
  result.select();
  document.execCommand("copy");
  alert("Copied to clipboard!");
}

function clearAll() {
  document.getElementById("text").value = "";
  document.getElementById("result").value = "";
}
