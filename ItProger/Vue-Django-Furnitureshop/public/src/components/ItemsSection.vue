<template>
  <section class="items-section">
    <div
      v-for="item in items"
      :key="item.slug"
      class="item-card"
    >
      <img :src="`/img/${item.image}`" :alt="item.title" />
      <h2>{{ item.title }}</h2>
      <p>{{ item.desc }}</p>

      <div class="card-footer">
        <span class="price">{{ item.price }}$</span>
        <button class="btn-cart" @click="handleBuy(item)">🛒 Купити</button>
      </div>

      <FormEdit :item="item" />
    </div>
  </section>
</template>

<script>
import FormEdit from './FormEdit.vue'

export default {
  name: 'ItemsSection',

  components: {
    FormEdit
  },

  props: {
    items: {
      type: Array,
      required: true
    }
  },

  emits: ['add-to-buy'],

  methods: {
    handleBuy(item) {
      this.$emit('add-to-buy', item); 
    }
  }
}
</script>

<style scoped>
.items-section {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  padding: 32px;
}

.item-card {
  background: #fff;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.07);
  display: flex;
  flex-direction: column;
}

.item-card img {
  width: 100%;
  height: 220px;
  object-fit: cover;
}

.item-card h2 {
  font-size: 20px;
  font-weight: 700;
  margin: 16px 16px 8px;
}

.item-card p {
  font-size: 14px;
  color: #444;
  margin: 0 16px 12px;
  flex: 1;
}

.card-footer {
display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px; 
  margin-top: auto;
  border-top: 1px solid #f0f0f0;
}

.price {
  font-size: 18px;
  font-weight: 600;
  color: #1a5c3a;
}

.btn-cart {
  background-color: #1a5c3a; 
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease; 
  display: flex;
  align-items: center;
  gap: 8px
}

.btn-cart:hover {
  background-color: #154d30;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transform: translateY(-1px); 
}

.btn-cart:active {
  transform: translateY(0);
}


:deep(.form-edit) {
  padding: 0 16px 16px;
}
</style>