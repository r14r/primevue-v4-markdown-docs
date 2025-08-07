<img alt="user header" class="w-full md:w-80 rounded mb-6" src="https://primefaces.org/cdn/primevue/images/card-vue.jpg" :style="filterStyle" />
<SelectButton v-model="filter" :options="filterOptions" optionLabel="label" optionValue="value" class="mb-4" />
<Slider v-model="filterValues[filter]" class="w-56" :min="0" :max="200" />