# 🐦 Twitter                   https://twitter.com/vandadnp
# 🔵 LinkedIn                  https://linkedin.com/in/vandadnp
# 🎥 YouTube                   https://youtube.com/c/vandadnp
# 🤝 Want to support my work?  https://buymeacoffee.com/vandad


from enum import IntFlag


class Access(IntFlag):
    CREATE_MEETING = 0b0001
    EDIT_MEETING = 0b0010
    DELETE_MEETING = 0b0100
    ADMIN_MEETING = 0b0111


admin = Access.ADMIN_MEETING
can_admin_delete_meeting = bool(admin & Access.DELETE_MEETING)
print(can_admin_delete_meeting)  # True

flags = [flag for flag in Access if flag in admin]
print(flags)
# [ <Access.CREATE_MEETING: 1>,
#   <Access.EDIT_MEETING: 2>,
#   <Access.DELETE_MEETING: 4>,
#   <Access.ADMIN_MEETING: 7>
# ]
