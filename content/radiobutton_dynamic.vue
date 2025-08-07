<div v-for="category in categories" :key="category.key" class="flex items-center gap-2">
    <RadioButton v-model="selectedCategory" :inputId="category.key" name="dynamic" :value="category.name" />
    <label :for="category.key">{{ category.name }}</label>
</div>