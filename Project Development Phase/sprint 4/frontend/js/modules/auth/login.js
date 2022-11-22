import { constants } from "../../constants.js";
import { alert } from "../../utils.js";

const loginForm = document.querySelector("#login-form");
const messageBox = document.querySelector(".message-box");
const loader = document.querySelector("#loader");
const backToLogin = document.querySelector("#back-to-login");
const resendMailOpen = document.querySelector("#resend-mail-open");
const resendMailForm = document.querySelector('#resend-mail-form');

loginForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  loader.classList.remove("d-none");
  const api_body = {
    email: e.target[0].value,
    password: e.target[1].value
  }
  login(api_body);
});

resendMailOpen.addEventListener('click', () => {
  loginForm.classList.add('d-none');
  resendMailForm.classList.remove('d-none');
  resetForm();
});

backToLogin.addEventListener('click', () => {
  loginForm.classList.remove('d-none');
  resendMailForm.classList.add('d-none');
  resetForm();
});

resendMailForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const api_body = {
    email: e.target[0].value
  }
  resendConfirmationMail(api_body);
})

const login = async (api_body) => {
  try {
    const { data } = await axios.post(
      `${constants.BASE_URL}/auth/login`,
      api_body);
    loader.classList.add("d-none");
    alert(messageBox, data.message, 'success');
    localStorage.setItem("token", data.data.jwt_token);
    window.location.href = 'index.html';
  } catch (error) {
    console.error("Login Error: ", error);
    loader.classList.add("d-none");
    alert(messageBox, error.response.data.message, 'failed');
  }
}

const resendConfirmationMail = async (api_body) => {
  try {
    const { data } = await axios.post(
      `${constants.BASE_URL}/auth/resend_confirmation_email`,
      api_body);
    alert(messageBox, data.message, 'success');
    resetForm();
  }
  catch (err) {
    alert(messageBox, error.response.data.message, 'failed');
  }
}

const resetForm = () => {
  const formInputs = document.querySelectorAll('input');
  formInputs.forEach((input) => {
    input.value = '';
  })
}
