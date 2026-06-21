<template>
  <div class="form-edit">
    <button class="btn-edit" @click="isOpen = !isOpen">
      Редагувати
    </button>

    <div v-if="isOpen" class="edit-form">
      <input
        v-model="image"
        type="text"
        placeholder="Фото товару (наприклад: chair.jpeg)"
      />
      <input
        v-model="title"
        type="text"
        placeholder="Назва товару"
      />
      <input
        v-model="desc"
        type="text"
        placeholder="Опис товару"
      />
      <input
        v-model="price"
        type="number"
        placeholder="Ціна"
      />
      <button class="btn-update" @click="handleUpdate">
        Оновити
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'FormEdit',

  props: {
    item: {
      type: Object,
      required: true
    }
  },

  data() {
    return {
      isOpen: false,
      image: this.item.image,
      title: this.item.title,
      desc: this.item.desc,
      price: this.item.price
    }
  },

  methods: {
    async handleUpdate() {
      await axios.put(`http://127.0.0.1:8000/api/edit-item/${this.item.slug}`, {
        image: this.image,
        title: this.title,
        desc: this.desc,
        price: this.price
      })
      window.location.reload()
    }
  }
}
</script>

<style scoped>
.form-edit {
  margin-top: 12px;
}

.btn-edit {
  width: 100%;
  padding: 12px;
  background-color: #1a5c3a;
  color: #fff;
  border: none;
  cursor: pointer;
  font-size: 15px;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.btn-edit:hover {
  background-color: #154d30;
}

.edit-form {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 10px;
}

.edit-form input {
  padding: 10px 12px;
  border: 1px solid #d0d0d0;
  font-size: 14px;
  outline: none;
}

.edit-form input:focus {
  border-color: #1a5c3a;
}

.btn-update {
  width: 100%;
  padding: 12px;
  background-color: #1a5c3a;
  color: #fff;
  border: none;
  cursor: pointer;
  font-size: 15px;
  font-weight: 500;
  letter-spacing: 0.5px;
}

.btn-update:hover {
  background-color: #154d30;
}
</style>