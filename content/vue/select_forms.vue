<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full md:w-56">
    <div class="flex flex-col gap-1">
        <Select name="city.name" :options="cities" optionLabel="name" placeholder="Select a City" fluid />
        <Message v-if="$form.city?.name?.invalid" severity="error" size="small" variant="simple">{{ $form.city.name.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>