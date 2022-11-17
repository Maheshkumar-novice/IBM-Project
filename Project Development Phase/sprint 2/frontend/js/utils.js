export function alert(element, message, status){
  element.classList.remove('d-none');
  element.classList.add(status);
  element.textContent = message;
  setTimeout(() => {
    element.classList.add('d-none');
  },3000);
}