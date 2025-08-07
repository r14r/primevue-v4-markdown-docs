<IftaLabel class="w-full md:w-56">
    <CascadeSelect v-model="selectedCity" inputId="cs_city" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" class="w-full" variant="filled" />
    <label for="cs_city">City</label>
</IftaLabel>