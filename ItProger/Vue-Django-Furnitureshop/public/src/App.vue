<script>
import { RouterView } from 'vue-router'
import axios from 'axios'

export default {
    data() {
        return {
            basket: [],
            items: []  
        }
    },
    methods: {
      addToBasket(item) {
        let found = false
        this.basket.forEach(el => {
            if(el.slug == item.slug) {
              found = true
              return
            }
        })
        if(found) return

        this.basket.push(item)
        localStorage.setItem("basket", JSON.stringify(this.basket))
      },
      deleteFromBasket(slug) {
        this.basket = this.basket.filter(el => {
          return el.slug != slug
        })
        localStorage.setItem("basket", JSON.stringify(this.basket))
      }
    },
async created() {
  const saved = localStorage.getItem("basket")
  if (saved && saved !== "null" && saved !== "") {
    this.basket = [...JSON.parse(saved)]
  }

  const res = await axios.get('http://127.0.0.1:8000/api/items/')
  this.items = res.data
}
}
</script>

<template>
  <div class="container">
    <RouterView
      :basket="basket"
      :addToBasket="addToBasket"
      :deleteFromBasket="deleteFromBasket"
      :items="items"
    />
  </div>
</template>
