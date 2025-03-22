from django.conf import settings
from stream_chat import StreamChat

class StreamChatService:
    def __init__(self):
        self.client = StreamChat(
            api_key=settings.STREAM_API_KEY,
            api_secret=settings.STREAM_API_SECRET
        )
    
    def generate_token(self, user_id):
        """Generate a Stream Chat token for a user"""
        return self.client.create_token(str(user_id))
    
    def upsert_user(self, user):
        """Create or update a user in Stream Chat"""
        user_type = "doctor" if user.user_type == "doctor" else "patient"
        return self.client.upsert_user({
            "id": str(user.id),
            "name": f"{user.first_name} {user.last_name}",
            "role": user_type,
            "image": "https://getstream.io/random_svg/?id=" + str(user.id)
        })
    
    def create_channel(self, channel_type, channel_id, members, name=None):
        """Create a new chat channel"""
        return self.client.channel(
            channel_type,
            channel_id,
            {
                "members": members,
                "name": name
            }
        )
    
    def get_or_create_channel(self, user1_id, user2_id):
        """Get or create a direct message channel between two users"""
        # Sort IDs to ensure consistent channel IDs
        members = sorted([str(user1_id), str(user2_id)])
        channel_id = f"{members[0]}-{members[1]}"
        
        try:
            # Try to get existing channel
            channel = self.client.channel("messaging", channel_id)
            channel.query()
            return channel
        except:
            # Create new channel if it doesn't exist
            return self.create_channel(
                "messaging", 
                channel_id, 
                members
            ) 