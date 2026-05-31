function refreshWhileStatusIsPending(interval = 5000) {
  const condition = !(currentStatus === "pending");

  function checkStatus() {
    if (condition) return true;
    setTimeout(() => {
      location.reload();
    }, interval);
    return false;
  }

  checkStatus();

  const checkInterval = setInterval(() => {
    if (condition) {
      clearInterval(checkInterval);
    }
  }, interval);
}