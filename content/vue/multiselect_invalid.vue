<MultiSelect v-model="selectedCities1" :options="cities" optionLabel="name" filter placeholder="Select Cities" 
        :maxSelectedLabels="3" :invalid="selectedCities1?.length === 0" class="w-full md:w-80" />
<MultiSelect v-model="selectedCities2" :options="cities" optionLabel="name" filter placeholder="Select Cities" 
        :maxSelectedLabels="3" :invalid="selectedCities2?.length === 0" class="w-full md:w-80" variant="filled" />