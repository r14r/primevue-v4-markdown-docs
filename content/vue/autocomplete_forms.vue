<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex justify-center flex-col gap-4 w-full md:w-56">
    <div class="flex flex-col gap-1">
        <AutoComplete name="country.name" optionLabel="name" :suggestions="filteredCountries" @complete="search" fluid />
        <Message v-if="$form.country?.name?.invalid" severity="error" size="small" variant="simple">{{ $form.country.name.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>