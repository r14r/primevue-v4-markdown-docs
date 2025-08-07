<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col items-center gap-2">
        <ColorPicker name="color" />
        <Message v-if="$form.color?.invalid" severity="error" size="small" variant="simple">{{ $form.color.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>