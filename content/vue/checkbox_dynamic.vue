<div v-for="category of categories" :key="category.key" class="flex items-center gap-2">
    <Checkbox v-model="selectedCategories" :inputId="category.key" name="category" :value="category.name" />
    <label :for="category.key">{{ category.name }}</label>
</div>