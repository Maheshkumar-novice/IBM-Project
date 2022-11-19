import { constants } from "../../constants.js";

const loader = document.querySelector("#loader");
const inventoriesWrapper = document.querySelector("#inventories");

const token = localStorage.getItem("token");
const requestHeaders = {
  headers: {
    Authorization: 'Bearer ' + token
  }
};

window.addEventListener('load', () => {
  loader.classList.remove('d-none');
  getInventory();
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