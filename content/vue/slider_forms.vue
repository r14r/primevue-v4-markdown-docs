<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4 w-full sm:w-56">
    <div class="flex flex-col gap-4">
        <Slider name="slider" />
        <Message v-if="$form.slider?.invalid" severity="error" size="small" variant="simple">{{ $form.slider.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>