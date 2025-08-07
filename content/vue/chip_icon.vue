<Chip label="Apple" icon="pi pi-apple" />
<Chip label="Facebook" icon="pi pi-facebook" />
<Chip label="Google" icon="pi pi-google" />
<Chip label="Microsoft" icon="pi pi-microsoft" removable />
<Chip label="GitHub" icon="pi pi-github" removable>
    <template #removeicon="{ removeCallback, keydownCallback }">
        <i class="pi pi-minus-circle" @click="removeCallback" @keydown="keydownCallback" />
    </template>
</Chip>