from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    portfolio_site = models.URLField(blank = True)
    
    def __str__(self):
        return self.user.username

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DashboardUserprofileinfo(models.Model):
    portfolio_site = models.CharField(max_length=200)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'dashboard_userprofileinfo'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PmaBroadcast(models.Model):
    id = models.BigAutoField(primary_key=True)
    applied = models.TextField(blank=True, null=True)  # This field type is a guess.
    broadcastid = models.CharField(db_column='broadcastId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField()
    eligible = models.TextField(blank=True, null=True)  # This field type is a guess.
    expirydate = models.DateTimeField(db_column='expiryDate')  # Field name made lowercase.
    overriddenby = models.CharField(db_column='overriddenBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    overridereason = models.CharField(db_column='overrideReason', max_length=255, blank=True, null=True)  # Field name made lowercase.
    demand_fk = models.ForeignKey('PmaDemand', models.DO_NOTHING, db_column='demand_fk')
    trainee_fk = models.ForeignKey('PmaTrainee', models.DO_NOTHING, db_column='trainee_fk')
    emailsent = models.TextField(db_column='emailSent')  # Field name made lowercase. This field type is a guess.
    screened = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pma_broadcast'


class PmaContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    crmid = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(db_column='firstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    mobile = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    partner_fk = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pma_contact'

class PmaPartner(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    crmid = models.CharField(unique=True, max_length=50)
    description = models.TextField()
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=100)
    logourl = models.TextField(db_column='logoUrl', blank=True, null=True)  # Field name made lowercase.
    noofemployees = models.CharField(db_column='noOfEmployees', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma_partner'        


class PmaDemand(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.TextField(blank=True, null=True)  # This field type is a guess.
    bonddetails = models.CharField(db_column='bondDetails', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bondduration = models.CharField(db_column='bondDuration', max_length=255, blank=True, null=True)  # Field name made lowercase.
    certification = models.CharField(max_length=255, blank=True, null=True)
    compensation = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(max_length=255, blank=True, null=True)
    jobtitle = models.CharField(db_column='jobTitle', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastgradyear = models.CharField(db_column='lastGradYear', max_length=200, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=255, blank=True, null=True)
    marks10 = models.FloatField(blank=True, null=True)
    marks12 = models.FloatField(blank=True, null=True)
    markspg = models.FloatField(db_column='marksPG', blank=True, null=True)  # Field name made lowercase.
    marksug = models.FloatField(db_column='marksUG', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    numberofpositions = models.IntegerField(db_column='numberOfPositions', blank=True, null=True)  # Field name made lowercase.
    specialconditions = models.CharField(db_column='specialConditions', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    contact_fk = models.BigIntegerField()
    partner_fk = models.ForeignKey(PmaPartner, on_delete = models.CASCADE)
    constraintlocation = models.CharField(db_column='constraintLocation', max_length=255)  # Field name made lowercase.
    jobdescription = models.CharField(db_column='jobDescription', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    aptitudegrade = models.FloatField(db_column='aptitudeGrade')  # Field name made lowercase.
    communicationgrade = models.CharField(db_column='communicationGrade', max_length=255)  # Field name made lowercase.
    technicalgrade = models.FloatField(db_column='technicalGrade')  # Field name made lowercase.
    premium = models.TextField()  # This field type is a guess.
    successindicatorscore = models.IntegerField(db_column='successIndicatorScore', blank=True, null=True)  # Field name made lowercase.
    applicationgap = models.IntegerField(db_column='applicationGap', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pma_demand'


class PmaDemandDegrees(models.Model):
    demand = models.ForeignKey(PmaDemand, models.DO_NOTHING, db_column='Demand_id')  # Field name made lowercase.
    degrees = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma_demand_degrees'


class PmaDemandSkills(models.Model):
    demand = models.ForeignKey(PmaDemand, models.DO_NOTHING, db_column='Demand_id')  # Field name made lowercase.
    skills = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pma_demand_skills'


class PmaDrive(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    demand_fk = models.ForeignKey(PmaDemand, models.DO_NOTHING, db_column='demand_fk')

    class Meta:
        managed = False
        db_table = 'pma_drive'


class PmaDriveRounds(models.Model):
    drive = models.OneToOneField(PmaDrive, models.DO_NOTHING, db_column='Drive_id', primary_key=True)  # Field name made lowercase.
    rounds = models.CharField(max_length=255, blank=True, null=True)
    round_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pma_drive_rounds'
        unique_together = (('drive', 'round_num'),)


class PmaNotificationLikes(models.Model):
    id = models.BigAutoField(primary_key=True)
    drive_fk = models.ForeignKey(PmaDrive, models.DO_NOTHING, db_column='drive_fk')
    likescount = models.BigIntegerField(db_column='likesCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pma_notification_likes'


class PmaOffer(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    drive_fk = models.BigIntegerField()
    trainee_fk = models.ForeignKey('PmaTrainee', models.DO_NOTHING, db_column='trainee_fk')
    offerdate = models.DateField(db_column='offerDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pma_offer'
        unique_together = (('status', 'drive_fk', 'trainee_fk'),)


class PmaPlacementCredits(models.Model):
    trainee_fk = models.BigIntegerField()
    credits = models.IntegerField()
    remarks = models.CharField(max_length=50, blank=True, null=True)
    enteredby = models.CharField(db_column='enteredBy', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pma_placement_credits'


class PmaSelectionRound(models.Model):
    id = models.BigAutoField(primary_key=True)
    contactdetails = models.CharField(db_column='contactDetails', max_length=1500)  # Field name made lowercase.
    date = models.CharField(max_length=10)
    roundnumber = models.IntegerField(db_column='roundNumber')  # Field name made lowercase.
    time = models.CharField(max_length=8)
    drive_fk = models.ForeignKey(PmaDrive, models.DO_NOTHING, db_column='drive_fk')

    class Meta:
        managed = False
        db_table = 'pma_selection_round'


class PmaTrainee(models.Model):
    id = models.BigAutoField(primary_key=True)
    batch = models.CharField(max_length=255)
    certification = models.CharField(max_length=255)
    communicationgrade = models.CharField(db_column='communicationGrade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=255)
    firstname = models.CharField(db_column='firstName', max_length=255)  # Field name made lowercase.
    gender = models.CharField(max_length=255, blank=True, null=True)
    lastgradyear = models.IntegerField(db_column='lastGradYear')  # Field name made lowercase.
    lastgraduation = models.CharField(db_column='lastGraduation', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=255)  # Field name made lowercase.
    marks10 = models.FloatField()
    marks12 = models.FloatField()
    markspg = models.FloatField(db_column='marksPG', blank=True, null=True)  # Field name made lowercase.
    marksug = models.FloatField(db_column='marksUG')  # Field name made lowercase.
    mobile = models.CharField(unique=True, max_length=255)
    projectgrade = models.CharField(db_column='projectGrade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    selfplacedwith = models.CharField(db_column='selfPlacedWith', max_length=255, blank=True, null=True)  # Field name made lowercase.
    skill = models.CharField(max_length=255)
    technicalgrade = models.CharField(db_column='technicalGrade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    traineeid = models.CharField(db_column='traineeId', unique=True, max_length=255)  # Field name made lowercase.
    verifiedby = models.CharField(db_column='verifiedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    placed_partner_fk = models.BigIntegerField(blank=True, null=True)
    enteredby = models.CharField(db_column='enteredBy', max_length=255)  # Field name made lowercase.
    updatedby = models.CharField(db_column='updatedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    aptitudegrade = models.CharField(db_column='aptitudeGrade', max_length=255, blank=True, null=True)  # Field name made lowercase.
    inactive = models.TextField(db_column='inActive')  # Field name made lowercase. This field type is a guess.
    validfrom = models.DateField(db_column='validFrom', blank=True, null=True)  # Field name made lowercase.
    validto = models.DateField(db_column='validTo', blank=True, null=True)  # Field name made lowercase.
    currentlocation = models.CharField(db_column='currentLocation', max_length=255)  # Field name made lowercase.
    collegename = models.CharField(db_column='collegeName', max_length=350, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(blank=True, null=True)
    yearofgrad = models.IntegerField(db_column='yearOfGrad', blank=True, null=True)  # Field name made lowercase.
    yearofinter = models.IntegerField(db_column='yearOfInter', blank=True, null=True)  # Field name made lowercase.
    yearofssc = models.IntegerField(db_column='yearOfSSC', blank=True, null=True)  # Field name made lowercase.
    offerdate = models.DateTimeField(db_column='offerDate', blank=True, null=True)  # Field name made lowercase.
    dateofjoining = models.CharField(db_column='dateOfJoining', max_length=255, blank=True, null=True)  # Field name made lowercase.
    backlogspg = models.IntegerField(db_column='backlogsPG')  # Field name made lowercase.
    backlogsug = models.IntegerField(db_column='backlogsUG')  # Field name made lowercase.
    collegenameug = models.CharField(db_column='collegeNameUG', max_length=255)  # Field name made lowercase.
    graduation = models.CharField(max_length=255)
    interboardname = models.CharField(db_column='interBoardName', max_length=255)  # Field name made lowercase.
    rollnumberpg = models.CharField(db_column='rollNumberPG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rollnumberug = models.CharField(db_column='rollNumberUG', max_length=255)  # Field name made lowercase.
    sscboardname = models.CharField(db_column='sscBoardName', max_length=255)  # Field name made lowercase.
    universitypg = models.CharField(db_column='universityPG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    universityug = models.CharField(db_column='universityUG', max_length=255)  # Field name made lowercase.
    yearofpg = models.IntegerField(db_column='yearOfPG', blank=True, null=True)  # Field name made lowercase.
    eamcetrank = models.CharField(db_column='eamcetRank', max_length=255)  # Field name made lowercase.
    photourl = models.CharField(db_column='photoUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pma_trainee'


class PmaTraineeComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    about = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    postedby = models.CharField(db_column='postedBy', max_length=255, blank=True, null=True)  # Field name made lowercase.
    trainee_fk = models.ForeignKey(PmaTrainee, models.DO_NOTHING, db_column='trainee_fk')

    class Meta:
        managed = False
        db_table = 'pma_trainee_comment'


class PmaTraineeDrivesRemaining(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    remaining = models.IntegerField()
    trainee_fk = models.ForeignKey(PmaTrainee, models.DO_NOTHING, db_column='trainee_fk')

    class Meta:
        managed = False
        db_table = 'pma_trainee_drives_remaining'


class PmaTraineeRound(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=255)
    updatedby = models.CharField(db_column='updatedBy', max_length=255)  # Field name made lowercase.
    selection_round_fk = models.ForeignKey(PmaSelectionRound, models.DO_NOTHING, db_column='selection_round_fk')
    trainee_fk = models.ForeignKey(PmaTrainee, models.DO_NOTHING, db_column='trainee_fk')

    class Meta:
        managed = False
        db_table = 'pma_trainee_round'