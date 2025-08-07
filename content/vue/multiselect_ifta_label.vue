<IftaLabel>
    <MultiSelect v-model="selectedCities" inputId="ms_cities" :options="cities" optionLabel="name" filter :maxSelectedLabels="3" class="w-full" variant="filled" />
    <label for="ms_cities">Cities</label>
</IftaLabel>