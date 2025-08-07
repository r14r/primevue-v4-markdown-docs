<Password v-model="value">
    <template #header>
        <div class="font-semibold text-xm mb-4">Reset Password</div>
    </template>
    <template #footer>
        <Divider />
        <ul class="pl-2 my-0 leading-normal text-sm">
            <li>At least one lowercase</li>
            <li>At least one uppercase</li>
            <li>At least one numeric</li>
            <li>Minimum 8 characters</li>
        </ul>
    </template>
</Password>