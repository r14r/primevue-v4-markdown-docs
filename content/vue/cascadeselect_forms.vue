<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex justify-center flex-col gap-4">
    <div class="flex flex-col gap-1">
        <CascadeSelect name="city" :options="countries" optionLabel="cname" optionGroupLabel="name" :optionGroupChildren="['states', 'cities']" class="w-56" placeholder="Select a City" />
        <Message v-if="$form.city?.invalid" severity="error" size="small" variant="simple">{{ $form.city.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>