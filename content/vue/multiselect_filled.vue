<MultiSelect v-model="selectedCities" variant="filled" :options="cities" optionLabel="name" filter placeholder="Select Cities"
    :maxSelectedLabels="3" class="w-full md:w-80" />