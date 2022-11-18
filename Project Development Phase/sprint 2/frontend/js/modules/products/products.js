import { constants } from "../../constants.js";
import { alert } from "../../utils.js";

const productsWrapper = document.querySelector("#products");
const loader = document.querySelector("#loader");
const formToggleBtn = document.querySelector("#form-toggle-btn");
const addProductForm = document.querySelector("#add-product-form");
const messageBox = document.querySelector(".message-box");

const token = localStorage.getItem("token");
const requestHeaders = {
  headers: {
    Authorization: 'Bearer ' + token
  }
};

window.addEventListener('load', () => {
  loader.classList.remove('d-none');
  getProducts();
});

formToggleBtn.addEventListener("click", () => {
  addProductForm.classList.toggle("d-none");
});

addProductForm.addEventListener("submit", (e) => {
  e.preventDefault();
  loader.classList.remove("d-none");
  const api_body = {
    name: e.target[0].value,
    description: e.target[1].value
  }
  addProduct(api_body);
});

const getProducts = async () => {
  try {
    const { data } = await axios.get(
      `${constants.BASE_URL}/products/all`,
      requestHeaders
    );
    createProductCards(data.data);
  }
  catch (error) {
    console.error("Get Products Error: ", error);
  }
  finally {
    loader.classList.add('d-none');
  }
}

const addProduct = async (api_body) => {
  try {
    const { data } = await axios.post(
      `${constants.BASE_URL}/products/`,
      api_body, requestHeaders);
    addProductForm.classList.add('d-none');
    alert(messageBox, data.message, 'success');
    getProducts();
    resetProductForm();
  }
  catch (error) {
    console.error("Add Product Error: ", error);
    alert(messageBox, error.response.data.message, 'failed');
  }
  finally {
    loader.classList.add("d-none");
  }
}

const createProductCards = (products) => {
  products.map((product) => {
    productsWrapper.innerHTML +=
      `<div class="product" id='card-${product.id}'>
      <div class="product-header">
        <h4 class="product-name">${product.name}</h4>
        <div>
          <button class="action-btn edit-btn" data-id=${product.id}>
            <i class="fas fa-pen"></i>
          </button>
          <button class="action-btn delete-btn" data-id=${product.id}>
            <i class="fas fa-trash"></i>
          </button>
          <button class="action-btn save-edit-btn d-none" data-id=${product.id}>
            <i class="fas fa-check"></i>
          </button>
        </div>
      </div>
      <p class="product-des">${product.description}</p>
    </div>`;
  });
}

const resetProductForm = () => {
  const formInputs = document.querySelectorAll('input');
  formInputs.forEach((input) => {
    input.value = '';
  })
}