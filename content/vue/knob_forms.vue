<Form v-slot="$form" :resolver="resolver" :initialValues="initialValues" @submit="onFormSubmit" class="flex flex-col gap-4">
    <div class="flex flex-col items-center gap-1">
        <Knob name="knob" />
        <Message v-if="$form.knob?.invalid" severity="error" size="small" variant="simple">{{ $form.knob.error?.message }}</Message>
    </div>
    <Button type="submit" severity="secondary" label="Submit" />
</Form>