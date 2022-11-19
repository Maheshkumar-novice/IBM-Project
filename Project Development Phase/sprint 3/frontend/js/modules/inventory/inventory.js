import { constants } from "../../constants.js";
import { alert } from "../../utils.js";


const loader = document.querySelector("#loader");
const inventoriesWrapper = document.querySelector("#inventories");
const formToggleBtn = document.querySelector("#form-toggle-btn");
const addInventoryForm = document.querySelector("#add-inventory-form");
const messageBox = document.querySelector(".message-box");
const productNameInput = document.querySelector('#product-name');
const locationNameInput = document.querySelector('#location-name');
const token = localStorage.getItem("token");
const requestHeaders = {
  headers: {
    Authorization: 'Bearer ' + token
  }
};

window.addEventListener('load', () => {
  loader.classList.remove('d-none');
  getProducts();
  getLocations();
  getInventory();
});

formToggleBtn.addEventListener("click", () => {
  addInventoryForm.classList.toggle("d-none");
});

addInventoryForm.addEventListener("submit", (e) => {
  e.preventDefault();
  loader.classList.remove("d-none");
  const api_body = {
    product_name: e.target[0].value,
    location_name: e.target[1].value,
    quantity: e.target[2].value,
    threshold: e.target[3].value
  }
  addInventory(api_body);
});

const getInventory = async () => {
  try {
    const { data } = await axios.get(
      `${constants.BASE_URL}/inventory/all`,
      requestHeaders
    );
    createInventoryCards(data.data);
  }
  catch (error) {
    console.error("Get Inventory Error: ", error);
  }
  finally {
    loader.classList.add('d-none');
  }
}

const addInventory = async (api_body) => {
  try {
    const { data } = await axios.post(
      `${constants.BASE_URL}/inventory/`,
      api_body, requestHeaders);
    addInventoryForm.classList.add('d-none');
    alert(messageBox, data.message, 'success');
    getInventory();
    resetInventoryForm();
  }
  catch (error) {
    console.error("Add Product Error: ", error);
    alert(messageBox, error.response.data.message, 'failed');
  }
  finally {
    loader.classList.add("d-none");
  }
}

const getProducts = async () => {
  try {
    const { data } = await axios.get(
      `${constants.BASE_URL}/products/all`,
      requestHeaders
    );
    createFormOptions(productNameInput,data.data)
  }
  catch (error) {
    console.error("Get Products Error: ", error);
  }
}


const getLocations = async () => {
  try {
    const { data } = await axios.get(
      `${constants.BASE_URL}/locations/all`,
      requestHeaders
    );
    createFormOptions(locationNameInput,data.data)
  }
  catch (error) {
    console.error("Get Products Error: ", error);
  }
}

const createInventoryCards = (inventories) => {
  inventoriesWrapper.innerHTML = '';
  inventories.map((inventory) => {
    inventoriesWrapper.innerHTML +=
      `<div class="item inventory" id='card-${inventory.id}'>
        <div class="item-header inventory-header">
          <h4 class="item-name inventory-product">${inventory.product.name}</h4>
          <div>
            <button class="action-btn edit-btn" data-id=${inventory.id}>
              <i class="fas fa-pen"></i>
            </button>
            <button class="action-btn delete-btn" data-id=${inventory.id}>
              <i class="fas fa-trash"></i>
            </button>
            <button class="action-btn save-edit-btn d-none" data-id=${inventory.id}>
              <i class="fas fa-check"></i>
            </button>
          </div>
        </div>
        <p class="item-des inventory-location">Location: <span>${inventory.location.name}</span></p>
        <p class="item-des inventory-quantity pt-0">Quantity: <span>${inventory.quantity}</span></p>
        <p class="item-des inventory-threshold pt-0">Threshold: <span>${inventory.threshold}</span></p>
      </div>`;
  });
}

const createFormOptions = (element, data) => {
  data.map((d) => {
    element.innerHTML +=
      `<option value=${d.name}>${d.name}</option>`
  })
}
const resetInventoryForm = () => {
  const formInputs = document.querySelectorAll('.app-input');
  formInputs.forEach((input) => {
    console.log(input);
    input.value = '';
  })
}