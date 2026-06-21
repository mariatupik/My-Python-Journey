<script>
import Header from '../components/Header.vue'
import HeadSection from '../components/HeadSection.vue'
import ItemsSection from '../components/ItemsSection.vue';

export default {
  props: ['basket', 'addToBasket', 'items'], 
  components: { Header, HeadSection, ItemsSection }
}
</script>

<template>
  <div>
    <Header :basket="basket" />
    <HeadSection />
    <ItemsSection :items="items" :addToBasket="addToBasket" /> 
  </div>
</template>